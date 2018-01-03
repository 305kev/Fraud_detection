"""
A set of functions that will process that data so that it can be used for model building.
"""

import pandas as pd

def load_data(filename):
    """
    Load the data in json format.
    :param filename: str, the relative path to a json file
    :return: df, a pandas dataframe of the json file
    """
    return pd.read_json(filename)


class DataProcessing():
    """
    A class that will handle all data preprocessing
    """
    def __init__(self, flag, df):
        """
        Instantiate the class.
        :param flag - Boolean, True indicates training data
        :param df - a pandas dataframe to be preprocessed
        """
        self.df = df
        self.train = flag

    def fit(self):
        """
        Controls the preprocessing process
        """
        if self.flag
            self._add_target()
        self._add_payout_length()
        self._add_venue_bool()
        self._convert_unix_to_datetime()
        self._unix_to_datetime()
#        self._payee_org_name()
        self._high_fraud_country()
        self._high_fraud_email_domain()
        # cols = ["fraud", "body_length","channels","delivery_method","fb_published",
        #         "gts","has_analytics","has_logo","name_length","num_order",
        #         "num_payouts", "org_twitter", "org_facebook", "sale_duration",
        #         "show_map", "user_age","fraud_country", "email_high_risk",
        #         "email_gmail", "email_medium_risk","payout_length", "venue_missing",
        #         "payee_org_iou"]
        cols = ["fraud", "body_length","channels","delivery_method","fb_published",
                "gts","has_analytics","has_logo","name_length","num_order",
                "num_payouts", "org_twitter", "org_facebook", "sale_duration",
                "show_map", "user_age","fraud_country", "email_high_risk",
                "email_gmail", "email_medium_risk","payout_length", "venue_missing"]
        self._keep_columns(cols)

    def _high_fraud_country(self):
        '''
        Identify the countries that has high fraud rate
        Country with entry > 15, and with fraud rate > 50%
        :return:
        '''
        countries = ["A1", "ID", "NA","PH","PK","VN"]
        self.df["fraud_country"] = self.df["country"].isin(countries)

    def _high_fraud_email_domain(self):
        '''
        Identify the email domain that has high fraud rate
        domains with entry > 15
        gmail is unique and is used as a separate column
        :return:
        '''
        high_risk = ["joonbug.com", "yahoo.fr", "rocketmail.com","live.fr","lidf.co.uk","ymail.com"]
        gmail_list = ["gmail.com"]
        medium_risk = ["hotmail.com","yahoo.com","hotmail.co.uk","live.com","aol.com","yahoo.co.uk"]
        self.df["email_high_risk"] = self.df["email_domain"].isin(high_risk)
        self.df["email_gmail"] = self.df["email_domain"].isin(gmail_list)
        self.df["email_medium_risk"] = self.df["email_domain"].isin(medium_risk)


    def._keep_columns(self, cols):
        self.df = self.df[cols]



    def _add_target(self):
        """
        Add class labels for the fraudulent transactions training data
        """
        self.df["fraud"] = 1 - self.df["acct_type"].eq("premium").mul(1)


    def _add_payout_length(self):
        """
        Add the number of previous payouts the organization has received
        """
        self.df["payout_length"] = self.df["previous_payouts"].str.len()


    def _add_venue_bool(self):
        """
        Add a Boolean that indicates whether or not all venue information is included.
        """
        self.df["venue_missing"] = df["venue_country"].isnull()

    def _unix_to_datetime(self, columns = ["approx_payout_date","event_created","event_end"]):
        '''
        Convert the columns of unix time to datetime object
        Input: DataFrame, columns to convert
        Output: DataFrame with columns converted to datetime object
        '''
        for column in columns:
            self.df[column] = pd.to_datetime(self.df[column], unit='s')
        pass

    # def _description_word_count(self,columns = ["description","org_desc"]):
    #     '''
    #     Creat two columns that counts the words in html input columns
    #     Name of the column is "column"_wc
    #     input: dataframe, the columns that contains html contents
    #     Return : datafram with addtional columns contains the word count for the description column
    #     '''
    #     for column in columns:
    #         n = self.df["acct_type"].count()
    #         self.df[column + "_wc"] = 0
    #         for i in range(2000):
    #             if i%1000 ==1:
    #                 print(i, float(i)/n)
    #             html = BeautifulSoup(self.df[column][i], "html.parser")
    #             self.df[column + "_wc"][i] = len(html.get_text().split(" "))
    #     pass
    def _payee_org_name(self):
        n = self.df["acct_type"].count()
        self.df["payee_org_iou"] = 0.0
        for i in range(n):
            if i%1000 == 1:
                print(i, float(i)/n)
            st1 = self.df["payee_name"][i]
            st2 = self.df["org_name"][i]
            if float(max(len(set(st1.split())),len(set(st2.split())))) > 0:
                self.df["payee_org_iou"][i] = len(set(st1.split()) & set(st2.split())) \
                                    /float(max(len(set(st1.split())),len(set(st2.split()))))
        pass


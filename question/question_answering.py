# description: Class for question answering, after being fed with a question
# and a context, it will return the answer to the question
# author: Kolade Gideon @Allaye
# created: 2022-10-10
# last modified: 2023-02-05 16:11:pm UTC

import json
from langdetect import  detect
import warnings
from typing import List, Union
from torch.cuda import is_available
from schema import Schema, SchemaError
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs



class QnA:
    def __init__(self, model_types='roberta', force_lang=False, model_name='deepset/roberta-base-squad2'):
        self.force_lang = force_lang
        self.result = None
        model_args = QuestionAnsweringArgs(n_best_size=2)

        self.model = QuestionAnsweringModel(model_types, model_name, args=model_args)

    def read_and_answer(self, data: List[dict]):
        """
        Performs context analysis and return answer to the question.
        Detects if input is not English, if non-English was detected terminates predictions.

        Args:
            - text (str): Statement to be read, with question to be answered
        """

        if self.force_lang:
            pass
        elif detect(data[0]['context']) != 'en':
            raise Exception(F"""{detect(data[0]['context'])}!!!, Non English text detected. Most questions and Answer model only works for English Lang,
            If you are certain the model can work with this input, please provide a True argument to the force_lang flag.""")

        # load and clean the data
        data = self.clean_up_date(data)
        # copy loaded data to output variable, the predict method is going to operate on the data inplace
        self.result = data
        # pass the data through the model for prediction
        prediction, logit = self.predict(data)
        # clean up the prediction and return the result by extracting predictions, and discard logits
        # add check predicted answer to it corresponding question
        result = self.clean_collate_predicted_result(prediction)
        return result

    def predict(self, data: List[dict]):
        """
        return predicted answer to a question along with their logit
        """
        predictions, logit = self.model.predict(data)
        return predictions, logit

    def clean_collate_predicted_result(self, predictions: list)->list:
        """
        Collect and prepare the predicted answer for display
        take each prediction and takeout the answer with the highest percentage and add it to the question dict,
        return a dict by default or a json file
        Note: even though this functions returns the answer with the higher prob, sometimes it isnt the most complete answer in the list

        Example output:
        Context: My friends calls me Kolade, i am a graduate studying Artificial intelligence with focus on CV and NLP"
        Question: what do i currently do?
        Answer: ['studying Artificial intelligence', 'graduate studying Artificial intelligence', 'a graduate studying Artificial intelligence',
                'Artificial intelligence', 'i am a graduate studying Artificial intelligence', 'graduate', 'a graduate',
                'studying Artificial intelligence with focus on CV and NLP'
        Prob_Value: [0.21937199808796254, 0.19993563159024388, 0.18636050051674263, 0.1808032702023698, 0.07728933828088122, 0.023925590006339308, 0.02249797173862308, 0.02097041553060479,
                    0.014455028508593676, 0.013174312490702719, 0.012279809507707259, 0.006253565134]
        looking at the above example the ans is current but it isnt the right answer.
        """
        counter = 0
        for idx, data in enumerate(self.result):
            for idx1, question in enumerate(data['qas']):
                predictions[counter]['answer'].remove("")
                self.result[idx]['qas'][idx1]['ans'] = predictions[counter]['answer'][0]
                counter += 1
        return self.result


    @staticmethod
    def clean_up_date(data: Union[str, list, dict], data_type: str = 'list')-> List[dict]:
        """
        perform cleanups and checks on data format,
        check if the data provided conform to the data_type
        """
        schema = Schema(
            [
                {
                    "context": str,
                    "qas": [
                        {
                            "question": str,
                            "id": str
                        }
                    ]
                }
            ]
        )
        if data_type not in ['dict', 'json', 'list']:
            warnings.warn('data_type provided might not be supported, are you sure about this?, '
                          'i will try and do the best i can with this', ResourceWarning)
        # this is the structure of all inference data, anything different will throw an error
        if type(data) == dict:
            data = [data]
            if not schema.is_valid(data):
                raise SchemaError(autos='Data Schema', errors=f'Inference Data Provided is not in the right format {schema}')
        elif type(data) is list:
            if not schema.is_valid(data):
                raise SchemaError(autos='Data Schema', errors=f'Inference Data Provided is not in the right format {schema}')
        else:
            f = open(data)
            data = json.load(f)
            if not schema.is_valid(data):
                raise SchemaError(autos='Data Schema', errors=f'Inference Data Provided is not in the right format {schema}')
        return data


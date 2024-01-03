import sys

model_path = './model'
sys.path.append(model_path)

from model import file_management
from model import data_processing

source_folders = [
    './broadcast_01/034',
    './broadcast_01/035'
]
db_folders = ['./CONVERSATION/CONVERSATION_01', './CONVERSATION/CONVERSATION_02', './CONVERSATION/CONVERSATION_03', './CONVERSATION/CONVERSATION_04']

# 모듈 이름을 통해 함수를 호출합니다.
file_management.create_folders(db_folders)
data_processing.process_data(source_folders, db_folders)
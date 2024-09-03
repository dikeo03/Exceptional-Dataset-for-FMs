from infilling_preprocess.masking_lyrics_korean import mask_all
from infilling_preprocess.evaluate_BERT_kor import evaluate_BERT_kor
from infilling_preprocess.get_list_for_gpt import get_list_for_gpt

from infilling_get_response_gemini import infilling_KOR
from evaluate_kor import evaluate_kor

if __name__ == '__main__':
    mask_all()
    evaluate_BERT_kor()

    get_list_for_gpt('./final_dataset/English_masking_task_words', 0.9)
    infilling_KOR("your own API Key", './final_Dataset/Korean_masking_task_words')

    evaluate_kor()

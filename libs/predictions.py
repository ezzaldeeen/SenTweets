from transformers import (
    pipeline,
    TFAutoModelForSequenceClassification,
    AutoTokenizer
)


def predict(texts: list[str]) -> list[dict]:
    """
    Predict the sentiment of the given text
    :param texts:
    :return:
    """
    # todo: separate the logic
    # todo: 1. model loader 2. actual prediction (for one sample) 3.
    # predefined labels
    labels = {
        "LABEL_0": "NEGATIVE",
        "LABEL_1": "NEUTRAL",
        "LABEL_2": "POSITIVE"
    }
    checkpoint = "models/cardiffnlp/twitter-roberta-base-sentiment"
    # getting pre-trained model
    model = TFAutoModelForSequenceClassification.from_pretrained(checkpoint)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    # setting up the sentiment analyzer pipline
    analyzer = pipeline(task="sentiment-analysis",
                        model=model,
                        tokenizer=tokenizer)
    predictions = analyzer(texts)

    outputs = []
    for prediction, text in zip(predictions, texts):
        output = {
            'text': text,
            'sentiment': labels[prediction['label']],
            'confidence':  prediction['score']
        }
        outputs.append(output)
    return outputs

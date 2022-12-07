from functools import reduce
from typing import Dict
from language.russian_conversion_map import russian_conversion_map, max_layer
from language.valid_words import ValidWordList

# converts the stream from keyboard strings to a condesed string
def stream_to_string(stream: list) -> str:
    return reduce(lambda a, b: a + b, stream)

# converts a stream into a partial translated string, looking at a specific layer of characters
# see examples below
def convert_layer(stream: list, layer: int, map: Dict[str, str]) -> str: 
    resulting_stream = []
    index = 0
    
    while index < len(stream):
        layer_stream = []
        if (index + layer <= len(stream)):
            for j in range(0, layer):
                layer_stream.append(stream[index + j])
        else:
            layer_stream.append(stream[index])
        if len(layer_stream) == layer:
            layer_string = stream_to_string(layer_stream)
            if layer_string in map:
                resulting_stream.append(map[layer_string])
                index += layer
            else:
                resulting_stream.append(stream[index])
                index += 1
        else:
            resulting_stream.append(stream[index])
            index += 1
    return resulting_stream

# translate the provided stream with layers of translation
# translates by looking at max_layer characters first, then max_layer-1 characters
# all the way down to 0, so that the translation is correct
def translate(stream: list, max_layer: int, map: Dict[str, str]) -> str:
    converting_stream = stream
    for layer in range(max_layer, 0, -1):
        converting_stream = convert_layer(converting_stream, layer, map)
    return stream_to_string(converting_stream)

# spell checks the translated output with a certain confidence level based on a valid word list
# returns the likely word
def spellcheck(output: str, valid_words: ValidWordList, confidence = 0.75) -> str:
    confidence_list = valid_words.generate_zeros()
    
    if (valid_words.contains(output)):
        return output
    
    len_output = len(output)
    for i in range(len(output)):
        for j in range(len(valid_words.valid_word_list)):
            test = valid_words.valid_word_list[j]
            len_test = valid_words.len_word_list[j]
            if (i < len_test):
                if output[i] == test[i]:
                    confidence_list[j] += (1 / len_test)
                else:
                    if (confidence_list[j] == 1):
                        confidence_list[j] -= (1 / (len_test * (1 / confidence)))
                    else:
                        confidence_list[j] -= (1 / len_test)
            else:
                confidence_list[j] -= (1 / len_output)
    
    return valid_words.generate_likely_word(confidence_list, confidence, output)
    
    

# tests for russian_conversion_model
if __name__ == "__main__":
    print(convert_layer(["s", "c", "h"], 1, russian_conversion_map))
    print(convert_layer(["s", "h"], 2, russian_conversion_map))
    print(convert_layer(["l", "s", "c", "h", "a", "p", "k", "a"], 3, russian_conversion_map))
    print(translate("p,r,i,v,e,t".split(","), max_layer, russian_conversion_map)) # works
    print(spellcheck("тебял", ValidWordList("../language/russian_words.txt")))

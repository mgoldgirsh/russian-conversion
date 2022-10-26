from functools import reduce
from typing import Dict
from russian_conversion_map import russian_conversion_map, max_layer

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

# tests for russian_conversion_model
if __name__ == "__main__":
    print(convert_layer(["s", "c", "h"], 1, russian_conversion_map))
    print(convert_layer(["s", "h"], 2, russian_conversion_map))
    print(convert_layer(["l", "s", "c", "h", "a", "p", "k", "a"], 3, russian_conversion_map))
    print(translate("p,r,i,v,e,t".split(","), max_layer, russian_conversion_map)) # works

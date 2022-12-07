# a class representing the characteristics of the valid word list 
class ValidWordList:
    
    # a valid word list holds a list of words and the length of each word associated with it 
    # in a seperate list as fields in the class
    def __init__(self, path: str, delim: str = "\n") -> None:
        f = open(path, 'r')
        self.valid_word_list = f.read().split(delim)
        f.close()
        self.len_word_list = list(map(lambda word: len(word), self.valid_word_list))
    
    # returns the string of the valid words list
    def __str__(self) -> str:
        return str(self.valid_word_list)
    
    # returns the item at the specified index of the valid words list
    def __getitem__(self, index: int) -> str:
        return self.valid_word_list[index]
    
    # sets the item at the specified index of the valid words list
    def __setitem__(self, index: int, item: str) -> None:
        self.valid_word_list[index] = item
    
    # generates a list of length of the valid word list, with 0s
    def generate_zeros(self) -> list:
        return list(map(lambda word_len: 0, self.len_word_list))
    
    # determines if the valid word list contains a specified word
    def contains(self, word: str) -> bool:
        return word in self.valid_word_list
    
    # generates the most similar word in the valid word list to the original word based on some confidence level
    # and some confidence list
    def generate_likely_word(self, confidence_list: list, confidence: float, original_word: str):
        # in case of a tie we pix the first one
        max_confidence = max(confidence_list)
        if (max_confidence > confidence):
            most_confident = confidence_list.index(max(confidence_list))
            print(max_confidence, self.valid_word_list[most_confident])
            
            return self.valid_word_list[most_confident]
        else:
            return original_word
        
    

# tests
if __name__ == "__main__":
    valid_list = ValidWordList("russian_words.txt")
    print(valid_list)
#!/usr/bin/env python3

def random_sentence_generator():
    return {
        subject: "",
        predicate: "",
        adjective: "",
        adverb_place: "",
        adverb_do: "",
        adverb_time: ""
    }

def main():
    data = random_sentence_generator()
    print("{subject} {predicate} {adjective} {adverb_place} {adverb_do} {adverb_time}".format(**data))

if __name__ == '__main__':
    main()
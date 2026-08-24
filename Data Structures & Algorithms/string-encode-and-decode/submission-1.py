class Solution:

    def __init__(self):
        self.delimiter = '|'

    def encode(self, strs: List[str]) -> str:
        total_strings = len(strs)
        header = str(total_strings) + self.delimiter
        body = ''

        # First number before the pipe tells us the
        # total number of strings, the elements that
        # follow tell us the length of each string
        #
        # input: ['string', 'data', 'here', 'now', '']
        # header: 3|6|4|4|3|0|
        # body: stringdataherenow
        # final string: "3|6|4|4|3|0|stringdataherenow"
        #
        # input: ['hello', 'world']
        # header: 2|5|5|helloworld
        for string in strs:
            header += str(len(string)) + self.delimiter
            body += string

        return header + body

    def decode(self, s: str) -> List[str]:
        chars = list(s)
        total_chars = len(chars)
        output = list()
        total_strings = ''
        pick_up_point = 0
        string_lengths = list()
        string_length = ''
        string = ''
        lengths_processed = 0

        # Determine total strings
        for i in range(0, total_chars):
            if chars[i] == self.delimiter:
                total_strings = int(total_strings)
                # Move needle to start at the next relevant char
                pick_up_point = i+1
                break

            total_strings += chars[i]

        # Get the lengths of each strings
        for i in range(pick_up_point, total_chars):
            if lengths_processed == total_strings:
                # Move the pick up point to next relevant char
                pick_up_point = i
                break

            if (chars[i] == self.delimiter):
                string_lengths.append(int(string_length))
                string_length = ''
                lengths_processed += 1
                continue

            string_length += chars[i]

        # Now that we know how many strings and their lengths
        # we can begin unpacking them into the list
        for length in string_lengths:
            string = ''
            str_end = pick_up_point + length

            if length > 0:
                for i in range(pick_up_point, str_end):
                    string += chars[i]
                    pick_up_point = str_end

            output.append(string)
            
        return output

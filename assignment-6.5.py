text = "X-DSPAM-Confidence:    0.8475";

new_text = text[text.find('0'): text.find('5') + 1]
# last_bit = new_text.rsplit(' ', )

as_float = float(text[text.find('0'): text.find('5') + 1])

print as_float

# Data type
intt1=50
intt2=70
float1=5.5
float2=8.5
string1= "bishakha"
string2= "bajracharya"
boolean1=True
boolean2=False


# Arithmetic Operation on int and float
integer_add = intt1 + intt2
float_add = float1 + float2
integer_product = intt1 * intt2
float_product = float1 * float2

# String concatenation
string_concatention = string1 + " " + string2

#Logical operation
boolean_and = boolean1 and boolean2
boolean_or = boolean1 or boolean2

# Dictionary to store 
data_dict = {
    "integer": [intt1, intt2, integer_add, integer_product],
    "float": [float1, float2, float_add, float_product],
    "string": [string1, string2, string_concatention],
    "boolean": [boolean1, boolean2, boolean_and, boolean_or]
}

# Display these variables by their types as keys
for data_type, values in data_dict.items():
    print(f"{data_type}: {values}")
    
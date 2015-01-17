#Determine whether a given string of parentheses is properly nested.
def solution(S):
    n = len(S)
    #base case: if S is empty tha is nested
    if n== 0:
        return 1
    #stack initialization
    stack = []
    #logic is: 
    #   if open bracket => ok 
    #   if close bracket => pop of last element, 
        #   if it doesn't match => return 0 
    i = 0
    while(i < len(S)):
        character = S[i]
        if character in ["]", "}", ")"]:
            if len(stack) == 0:
                return 0
            else:
                last_inserted_character = stack.pop()
                if (character == "]" and last_inserted_character != "["):
                    return 0
                if (character == ")" and last_inserted_character != "("):
                    return 0
                if (character == "}" and last_inserted_character != "{"):
                    return 0
        else:
            # character is [ ( or {
            stack.append(character)
        i+=1
    return 1

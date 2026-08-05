def number_pattern(n):

    pattern = []

    if not isinstance(n, int):

        return 'Argument must be an integer value.'

    else:

        if n < 1:

            return 'Argument must be an integer greater than 0.'
        
        else:

            for i in range(1, n + 1):
                
                pattern.append(str(i))
            
            joined = " ".join(pattern)
    
            return joined       
    
print(number_pattern(4))
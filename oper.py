# a simple clamp function
clamp = lambda x, mn, mx: mx if x > mx else (mn if x < mn else x)

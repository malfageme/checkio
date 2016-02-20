def checkio(data):
    return (data[0] if len(data) > 0 else 0 ) + ( checkio (data[1:])  if len(data) > 1 else 0 )


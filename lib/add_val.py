class Add_Val:
  def __init__(self, data_str: str):
    self.data_str = data_str

  def get_val(self, element, key: str, df, attr):
    if element:
      if self.data_str == 'text':
        value = element.text.strip()
      else:
        value = element.get(self.data_str)
        
      df.append(value)

      attr[key] = df
          
      print(f"Success! Value: {value}")
    else:
      print(f"{key} Element not found")
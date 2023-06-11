from ExtractTable import ExtractTable #pip install it
import pandas as pd #pip install it
et_sess = ExtractTable(api_key='use the API-key')        # Replace your VALID API Key here
print(et_sess.check_usage())        # Checks the API Key validity as well as shows associated plan usage 
table_data = et_sess.process_file(filepath='the file path', output_format="df")
table_data[0].to_excel('the new xlsx file path and name (example: MATH\GRADE_3\math_3_D_SECOND.xlsx)', index=False)#index false to prevent adding new column for indexing

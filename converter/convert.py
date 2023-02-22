import sys
from getopt import getopt
import re
import pandas as pd
from datetime import datetime

ENTRY_PATTERN = r'entry\((.+)\)'

def parse_args(argv):
  input_file_path = ''
  output_file_path = ''
   
  opts, _ = getopt(argv, 'i:o:h', ['input=', 'output=', 'help'])
   
  for opt, arg in opts:
    if opt in ('-h', '--help'):
      print('convert.py -i <input_file_path> -o <output_file_path>')
      sys.exit()
    elif opt in ('-i', '--input'):
      input_file_path = arg
    elif opt in ('-o', '--output'):
      output_file_path = arg
         
  if input_file_path == '' or output_file_path == '':
    print('Please provide an input and output file.')
    print('convert.py -i <input_file_path> -o <output_file_path>')
    sys.exit()
       
  print(f'Input file path: {input_file_path}')
  print(f'Output file path: {output_file_path}')
       
  return (input_file_path, output_file_path)

def parse_entry(line):
  matches = re.findall(ENTRY_PATTERN, line)
  if matches:
    return matches[0].replace(' ', '').split(',')
    
  print('No entry found. Skipping line...')
  return None

def build_dataframe(entries):
  df = pd.DataFrame(entries)
  df.columns = ['timestamp', 'event_type', 'workflow', 'case_id', 'activity', 'number']

  df.drop(['timestamp', 'workflow'], axis=1, inplace=True)

  df = df[(df['event_type'] != 'begin_of_process') & (df['event_type'] != 'end_of_process')]
  df.reset_index(drop=True, inplace=True)

  df.loc[df['event_type'] == 'begin_of_activity', 'event_type'] = 'start'
  df.loc[df['event_type'] == 'end_of_activity', 'event_type'] = 'complete'

  return df

if __name__ == '__main__':
  input_file_path, output_file_path = parse_args(sys.argv[1:])
  
  with open(input_file_path, 'r') as f:
    lines = [line.rstrip() for line in f]

  entries = []
  for line in lines:
    entry = parse_entry(line)
    if entry:
      entries.append(entry)

  df = build_dataframe(entries)
  df.to_csv(output_file_path, columns=['case_id', 'event_type', 'activity', 'number'], index=False)

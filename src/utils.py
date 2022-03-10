def print_shape_and_head_and_column_types(df, n):
    print('Shape:')
    print(f'({df.shape[0]} Rows, {df.shape[1]} Columns) \n')

    print(f'First {n} rows:')
    print(df.head(n))

    print('\nColumn types:')
    print(df.dtypes)

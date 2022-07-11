from app.generator import Generator

if __name__ == '__main__':
    print('Start zip generation...')
    Generator().generate_zip_files(50, 100, './temp/')
    print('Done.')

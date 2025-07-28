from datetime import datetime
from runner import Runner


def main():
    runner = Runner()

    start_time = datetime.now()
    print('\n[+] COR Initiated at:', start_time.isoformat())
    
    runner.classify()
    
    end_time = datetime.now()
    print('\n[+] COR Execution Completed at:', end_time.isoformat())


if __name__ == "__main__":
    main()

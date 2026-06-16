
import argparse
from lib.generate_log import generate_log

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("add-task")
    subparsers.add_parser("complete-task")
    
    args = parser.parse_args()
    
    if args.command == "add-task":
       generate_log(["Task created"])

    elif args.command == "complete-task":
       generate_log(["Task completed"])

if __name__ == "__main__":
    main()
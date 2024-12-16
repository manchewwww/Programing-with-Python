import sys
import asyncio
from api.fetch import fetch_trending, fetch_all_trending
from utils.validation import validate_arguments
from utils.output import save_as_csv, save_as_json


def main():
    if not validate_arguments(sys.argv):
        print("Usage: python main.py [tv|movies|all] [day|week] [csv|json]")
        sys.exit(1)

    media_type, time_window, output_format = sys.argv[1], sys.argv[2], sys.argv[3]

    if media_type == "all":
        trending_data = asyncio.run(fetch_all_trending(time_window))
    else:
        trending_data = asyncio.run(fetch_trending(media_type, time_window))

    # Sort data by rating (descending)
    sorted_data = sorted(trending_data, key=lambda x: x["rating"], reverse=True)
    
    # Output in the desired format
    if output_format == "csv":
        save_as_csv(sorted_data)
        print("Data saved to output.csv")
    elif output_format == "json":
        save_as_json(sorted_data)
        print("Data saved to output.json")


if __name__ == "__main__":
    main()


# ask for venv\Scripts\activate.bat
from multimodal_search import MultimodalSearch
from IPython.display import display, Image

def main():
    # Instantiate the class
    mm_search = MultimodalSearch()

    # Perform a search
    query = "jacket"
    results = mm_search.search(query=query, top_k=3)

    # Display the results and images
    for result in results:
        print(f"Score: {result.score}")
        display(Image(filename=result.content))

if __name__ == "__main__":
    main()
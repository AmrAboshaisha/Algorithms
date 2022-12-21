#include <iostream>
#include <fstream>
#include <string>

#include <podofo/podofo.h>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <PDF file>" << endl;
        return 1;
    }

    // open the PDF file
    PoDoFo::PdfMemDocument document(argv[1]);

    // get the number of pages in the PDF file
    int num_pages = document.GetPageCount();

    // iterate over the pages
    for (int i = 0; i < num_pages; i++) {
        // get the current page
        PoDoFo::PdfPage* page = document.GetPage(i);

        // get the page's size
        PoDoFo::PdfRect size = page->GetMediaBox();

        // create a content parser
        PoDoFo::PdfContentsTokenizer tokenizer(page);

        // create a content parser
        PoDoFo::PdfContentsTokenizer tokenizer(page);

        // read the tokens from the page
        while (tokenizer.ReadNext()) {
            // get the current token
            const PoDoFo::PdfVariant& token = tokenizer.GetNextVariant();

            // if the token is a string, print it
            if (token.IsString()) {
                cout << token.GetString().GetStringUtf8() << " ";
            }
        }

        // print a newline at the end of the page
        cout << endl;
    }

    return 0;
}

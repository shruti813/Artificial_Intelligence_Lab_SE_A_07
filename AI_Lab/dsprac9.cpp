// flight.cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <limits>

using namespace std;

const int MAX_CITIES = 10;

class flight {
public:
    int am[MAX_CITIES][MAX_CITIES];     // adjacency matrix (directed)
    string city_index[MAX_CITIES];      // city names
    flight();
    int create();                       // returns number of cities used
    void display(int city_count);
};

flight::flight() {
    for (int i = 0; i < MAX_CITIES; ++i) {
        city_index[i] = "";
        for (int j = 0; j < MAX_CITIES; ++j)
            am[i][j] = 0;
    }
}

int flight::create() {
    int city_count = 0;
    char c = 'y';
    while (c == 'y' || c == 'Y') {
        string s, d;
        cout << "\nEnter Source City: ";
        cin >> s;
        cout << "Enter Destination City: ";
        cin >> d;

        int si = -1, di = -1;
        // find existing indexes
        for (int i = 0; i < city_count; ++i) {
            if (city_index[i] == s) si = i;
            if (city_index[i] == d) di = i;
        }

        // add source if new
        if (si == -1) {
            if (city_count < MAX_CITIES) {
                city_index[city_count] = s;
                si = city_count++;
            } else {
                cout << "City limit reached. Cannot add \"" << s << "\".\n";
                // skip this iteration
                cout << "Do you want to continue adding? (y/n): ";
                cin >> c;
                continue;
            }
        }

        // add destination if new
        if (di == -1) {
            if (city_count < MAX_CITIES) {
                city_index[city_count] = d;
                di = city_count++;
            } else {
                cout << "City limit reached. Cannot add \"" << d << "\".\n";
                cout << "Do you want to continue adding? (y/n): ";
                cin >> c;
                continue;
            }
        }

        // read distance with validation
        int wt;
        cout << "Enter Distance from " << s << " to " << d << ": ";
        while (!(cin >> wt) || wt < 0) {
            cout << "Please enter a non-negative integer for distance: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        // set directed edge weight
        am[si][di] = wt;

        cout << "\nDo you want to add more cities/edges? (y/n): ";
        cin >> c;
    }
    return city_count;
}

void flight::display(int city_count) {
    if (city_count == 0) {
        cout << "\nNo cities/edges to display.\n";
        return;
    }

    cout << "\nDisplaying adjacency matrix:\n\n\t";
    // header
    for (int i = 0; i < city_count; ++i)
        cout << setw(8) << city_index[i];
    cout << "\n";

    // rows
    for (int i = 0; i < city_count; ++i) {
        cout << setw(8) << city_index[i];
        for (int j = 0; j < city_count; ++j) {
            cout << setw(8) << am[i][j];
        }
        cout << "\n";
    }
}

int main() {
    flight f;
    int city_count = f.create();
    f.display(city_count);
    return 0;
}

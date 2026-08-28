class DynamicArray {
public:
    int* arr;
    int cap;
    int size;

    DynamicArray(int capacity) {
        cap = capacity;
        arr = new int[cap];
        size = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size==cap) {
            resize();
        }
        arr[size] = n;
        ++size;
    }

    int popback() {
        --size;
        return arr[size];
    }

    void resize() {
        int newCap = 2 * cap;
        int* newArr = new int[newCap];

        for (int i=0; i<size; ++i) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
        cap = newCap;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return cap;
    }
};

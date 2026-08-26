int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: mandelbrot N\n";
        exit(1);
    }

    int N = atoi(argv[1]);
    if (N < 200) {
        std::cerr << "Error: N must be >= 200\n";
        exit(1);
    }

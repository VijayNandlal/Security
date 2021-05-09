#include <opencv2/video.hpp>
#include <opencv2/videoio/videoio.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {

	VideoCapture cap = VideoCapture(0);
	Mat frame;

	while (true){

		if (!cap.isOpened()) {
			cerr << "ERROR! Unable to open camera\n";
			return -1;
		}

		cout << "Start grabbing" << endl << "Press any key to terminate" << endl;

		cap.read(frame);

		if (frame.empty()) {
			cerr << "ERROR! blank frame grabbed\n";
			break;
		}

		imshow("Live", frame);

		if (waitKey(5) >= 0)
			break;
	}

	return 0;
}

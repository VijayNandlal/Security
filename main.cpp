#include <opencv2/video.hpp>
#include <opencv2/videoio/videoio.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/objdetect.hpp>
#include <opencv2/core/types.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {

	VideoCapture cap = VideoCapture(0);
	Mat frame;
	CascadeClassifier face_detect = CascadeClassifier("C:\\OpenCv\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml");

	while (true){

		if (!cap.isOpened()) {
			cerr << "ERROR! Unable to open camera\n";
			return -1;
		}

		cap.read(frame);

		if (frame.empty()) {
			cerr << "ERROR! blank frame grabbed\n";
			break;
		}

		Mat grayImage;
		cvtColor(frame, grayImage, COLOR_BGR2GRAY); 

		if (face_detect.empty()) {
			fprintf(stderr, "Faces profile could not be loaded");
			exit(1);
		}

		vector<Rect> faces;
		face_detect.detectMultiScale(grayImage, faces, 1.2, 10);

		for (int i = 0; i < faces.size(); i++) {
			rectangle(frame, faces[i], Scalar(255, 255, 0), 4);
		}


		imshow("Live", frame);

		if (waitKey(5) >= 0)
			break;
	}

	return 0;

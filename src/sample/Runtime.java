package sample;

import org.opencv.core.*;
import org.opencv.highgui.HighGui;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.videoio.*;
import org.opencv.imgproc.*;
import java.time.LocalTime;

import java.util.List;
import javafx.scene.image.ImageView;
import static org.opencv.highgui.HighGui.imshow;
import static org.opencv.highgui.HighGui.waitKey;
import static org.opencv.imgproc.Imgproc.rectangle;

public class Runtime {

    public static int begin(ImageView place, String location){

        VideoCapture cap = new VideoCapture(0);

        Mat frame = new Mat();

        CascadeClassifier face_detect = new CascadeClassifier("src/cascade/haarcascade_frontalface_default.xml");
        CascadeClassifier upper_body = new CascadeClassifier("src/cascade/haarcascade_upperbody.xml");

        LocalTime time = LocalTime.now();

        while(true){
            if(!cap.isOpened()){
                return 1;
            }

            cap.read(frame);

            if(frame.empty()){
                return 1;
            }

            Mat grey_image = new Mat();
            Imgproc.cvtColor(frame, grey_image, Imgproc.COLOR_BGR2GRAY);

            if (face_detect.empty()){
                return 1;
            }

            MatOfRect face_holder = new MatOfRect();
            MatOfRect upper_holder = new MatOfRect();

            face_detect.detectMultiScale(grey_image, face_holder, 1.2, 3);
            upper_body.detectMultiScale(grey_image, upper_holder, 1.2, 3);

            int flag = 1;

            List<Rect> hol = face_holder.toList();
            List<Rect> up_hol = upper_holder.toList();

            if (hol.size() == 0 && up_hol.size() == 0){
                flag = 0;
            }

            for(int i = 0 ; i < hol.size(); i++){
                rectangle(frame, hol.get(i), new Scalar(255, 255, 0), 4);
            }

            for(int j = 0; j < up_hol.size(); j++){
                rectangle(frame, up_hol.get(j), new Scalar(0, 255, 0), 2);
            }

            if (flag == 1 && time.compareTo(LocalTime.now().minusMinutes(2)) < 0) {
                Imgcodecs.imwrite(location, frame);
                time = LocalTime.now();
            }

            imshow("Live", frame);

            if (waitKey(5) == ' ') {
                HighGui.destroyAllWindows();
                break;

            }
        }


        return 0;
    }
}

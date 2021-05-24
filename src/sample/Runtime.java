package sample;

import javafx.scene.image.Image;
import org.opencv.core.*;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.videoio.*;
import org.opencv.imgproc.*;

import java.util.ArrayList;
import java.util.List;
import javafx.scene.image.ImageView;
import static org.opencv.highgui.HighGui.imshow;
import static org.opencv.highgui.HighGui.waitKey;
import static org.opencv.imgproc.Imgproc.rectangle;

public class Runtime {

    public static int begin(ImageView place){

        VideoCapture cap = new VideoCapture(0);

        Mat frame = new Mat();

        CascadeClassifier face_detect = new CascadeClassifier("C:\\OpenCv\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml");

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

            MatOfRect holder = new MatOfRect();
            face_detect.detectMultiScale(grey_image, holder, 1.2, 10);

            List<Rect> hol = holder.toList();
            for(Integer i = 0 ; i < hol.size(); i++){
                rectangle(frame, hol.get(i), new Scalar(255, 255, 0), 4);
            }

            imshow("Live", frame);



            if (waitKey(1) >= 0) {
                break;

            }
        }


        return 0;
    }
}

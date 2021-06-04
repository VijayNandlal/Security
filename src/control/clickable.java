package control;

import static sample.Runtime.begin;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;

import static javafx.application.Platform.exit;

public class clickable {
    @FXML
    private Button ignition;
    private ImageView view;
    private TextField texts;

    public void ignitionAction(){

        String path = texts.getText();
        if (path.compareTo("") == 0){
            path = "src/results/person.jpg";
        }

        int result = begin(view, path);

    }
}

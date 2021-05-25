package control;

import static sample.Runtime.begin;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.image.ImageView;

import static javafx.application.Platform.exit;

public class clickable {
    @FXML
    private Button ignition;
    private ImageView view;

    public void ignitionAction(){

        int result = begin(view);

    }
}

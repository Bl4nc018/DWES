package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class GameViewHolder extends RecyclerView.ViewHolder{
    // Aquí nos encontramos los elementos de la vista de la celda
    private TextView name;
    private ImageView game;

    // Este constructor recibe la vista de la celda e inicializa los atributos con los elementos de la misma.
    public GameViewHolder(@NonNull View ivi) {
        super(ivi);
        name = ivi.findViewById(R.id.text_view_game);
        game = ivi.findViewById(R.id.image_view_game);
    }
    // Y en este último método se muestran los datos en la vista de la celda:
    public void showData(GameData gameData) {
        this.name.setText(gameData.getName()); // Establecemos el nombre del juego en el TextView
        Util.downloadBitmapToImageView(gameData.getImage_url(), this.game); // Empleamos una utilidad para descargar y establecer la imagen del juego en el ImageView.
    }
}

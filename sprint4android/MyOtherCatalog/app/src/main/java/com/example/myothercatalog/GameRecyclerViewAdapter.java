package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class GameRecyclerViewAdapter extends RecyclerView.Adapter<GameViewHolder>{
    private List<GameData> games;
    private Activity activity;

    // Este es el constructor que recibe la lista de datos y la actividad asociada.
    public GameRecyclerViewAdapter(List<GameData> dataSet, Activity activity) {
        this.games=dataSet;
        this.activity=activity;
    }

    @NonNull
    @Override
    // El siguiente método es llamado cuando se necesita crear una nueva instancia de GameViewHolder
    public GameViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // La siguiente línea infla la vista del diseño de la celda y crea un nuevo GameViewHolder con esta.
        View gameView = LayoutInflater.from(parent.getContext()).inflate(R.layout.game_recycler_cell, parent, false);
        return new GameViewHolder(gameView);
    }

    @Override
    // En este método siguiente, es llamado para actualizar el contenido de un GameViewHolder específico.
    public void onBindViewHolder(@NonNull GameViewHolder holder, int position) {
        // Aquí obtenemos los datos correspondientes de la lista y llama al método showData en el GameViewHolder
        GameData dataForThisCell = games.get(position);
        holder.showData(dataForThisCell);
    }

    @Override
    // En el siguiente método, devolvemos el número total de elementos en la lista de juegos.
    public int getItemCount() { return games.size(); }

}

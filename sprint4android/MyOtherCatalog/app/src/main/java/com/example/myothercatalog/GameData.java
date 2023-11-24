package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class GameData {

    // En las siguientes variables, métodos get y en el método constructor, empleamos las variables
    // de los datos que el programa se va a encontrar en el JSON. Al final, haremos un método para
    // extrare y asignar los valores del objeto JSON a los atributos de la clase.

    private String name;
    private String descripcion;
    private String image_url;

    public String getName() {return name;}
    public String getDescripcion() {return descripcion;}
    public String getImage_url() {return image_url;}

    public GameData(String name, String descripcion, String image_url){
        this.name=name;
        this.descripcion=descripcion;
        this.image_url=image_url;
    }

    public GameData(JSONObject json){
        try{
            this.name = json.getString("name");
            this.descripcion = json.getString("descripcion");
            this.image_url = json.getString("image_url");
        }catch (JSONException e){ e.printStackTrace(); }
    }

}

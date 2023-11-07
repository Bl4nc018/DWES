package com.example.mycatalog;

import android.os.Bundle;
import android.view.MenuItem;

import androidx.annotation.NonNull;
import androidx.annotation.StringRes;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.Fragment;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {
    private DrawerLayout drawerLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog); // Establece el contenido de la actividad con el diseño de "activity_catalog.xml".

        Toolbar toolbar = findViewById(R.id.toolbar); // Encuentra y establece la barra de herramientas (Toolbar) en la actividad.
        setSupportActionBar(toolbar);

        drawerLayout = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawerLayout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);

        // Encuentra el DrawerLayout y configura un ActionBarDrawerToggle que maneja la apertura y cierre del cajón.
        // Este está vinculado a la Toolbar y utiliza los recursos de cadena definidos en "R.string" para las etiquetas
        // de apertura y cierre del cajón.

        drawerLayout.addDrawerListener(toggle); // Agrega un oyente al cajón de navegación para sincronizar su estado con el ActionBar.
        toggle.syncState();

        // Agregamos la vista de navegación (NavigationView) en la actividad y la asignamos como oyente de selección de elementos de navegación.
        NavigationView navigationView = findViewById(R.id.navigation_view);
        navigationView.setNavigationItemSelectedListener(this);

    }


    @Override
    public void onBackPressed() { // OnBackPressed se llama cuando el botón "Atrás" del dispositivo se presiona.
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
        // Este verifica si el drawer está abierto en el lado izquierdo ("START"). Si está abierto, lo cierra para ocultar el cajón.
            drawerLayout.closeDrawer(GravityCompat.START);
        } else {
        // Pero si el drawer no está abierto, se llama a "super.onBackPressed()".
        // Lo cual, resumidamente, permite volver a la actividad anterior o cerrar la app si no hay actividades anteriores.
            super.onBackPressed();
        }
    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
        // Obtiene la ID del título seleccionado del menú
        int titleId = getTitle(menuItem);

        // Llama al método showFragment para mostrar el fragmento correspondiente
        showFragment(titleId);

        // Cierra el cajón de navegación después de seleccionar un elemento
        drawerLayout.closeDrawer(GravityCompat.START);

        // Devuelve true para indicar que la selección se ha manejado correctamente
        return true;
    }

    private int getTitle(@NonNull MenuItem menuItem) {
        // Obtiene el título del elemento del menú como una cadena
        String itemId = (String) menuItem.getTitle();

        // Compara el título con las cadenas "Catalog" y "About" y devuelve la ID de recurso correspondiente
        if (itemId.equals("Catalog")) {
            return R.string.CatalogFragment;
        } else if (itemId.equals("About")) {
            return R.string.AboutFragment;
        }

        // Valor predeterminado si no se encuentra una coincidencia
        return 0;
    }

    private void showFragment(@StringRes int titleId) {
        Fragment fragment; // Inicializa el fragmento para su siguiente uso.
        if (titleId == R.string.CatalogFragment) {  // Comprueba si la ID del título coincide con la del CatalogFragment.
            // Muestra el fragmento CatalogFragment, proporcionandole la id para que pueda crearse adecuadamente.
            fragment = CatalogFragment.newInstance();
            // Comienza una transacción de fragmento, reemplaza el contenido del contenedor (R.id.home_content)
            // con el fragmento actual (fragment) y confirma la transacción.
            getSupportFragmentManager().beginTransaction().replace(R.id.home_content, fragment).commit();
            setTitle(getString(titleId));
        }
        // Comprueba si la ID del título coincide con la del AboutFragment.
        else if (titleId == R.string.AboutFragment){
            // Muestra el fragmento AboutFragment, igual que arriba.
            fragment = AboutFragment.newInstance();
            getSupportFragmentManager().beginTransaction().replace(R.id.home_content, fragment).commit();
            setTitle(getString(titleId));
        }
    }
}

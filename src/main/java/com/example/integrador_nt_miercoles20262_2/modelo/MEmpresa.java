package com.example.integrador_nt_miercoles20262_2.modelo;

import jakarta.persistence.*;

import java.util.UUID;

@Entity
@Table(name = "empresa")
public class MEmpresa {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    @Column(length = 60, nullable = false)
    private String nombre;
    @Column(length = 10, nullable = false)
    private String nit;
    @Column(length = 20, nullable = false)
    private String sector;
    @Column(length = 10, nullable = false)
    private String contacto;
    @Column(length = 30, nullable = false)
    private String correo;
    @Column(length = 10, nullable = false)
    private String telefono;
    @Column(nullable = false)
    private boolean activo;

    public MEmpresa() {
    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNit() {
        return nit;
    }

    public void setNit(String nit) {
        this.nit = nit;
    }

    public String getSector() {
        return sector;
    }

    public void setSector(String sector) {
        this.sector = sector;
    }

    public String getContacto() {
        return contacto;
    }

    public void setContacto(String contacto) {
        this.contacto = contacto;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }

    public MEmpresa(UUID id, String nombre, String nit, String sector, String contacto, String correo, String telefono, boolean activo) {
        this.id = id;
        this.nombre = nombre;
        this.nit = nit;
        this.sector = sector;
        this.contacto = contacto;
        this.correo = correo;
        this.telefono = telefono;
        this.activo = activo;
    }
}

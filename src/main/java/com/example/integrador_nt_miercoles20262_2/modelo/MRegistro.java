package com.example.integrador_nt_miercoles20262_2.modelo;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.util.UUID;

@Entity
@Table(name = "registro")
public class MRegistro {
    @Id 
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;
    @Column(length = 10, nullable = false)
    private LocalDate fecha_registro;
    @Column(length = 90, nullable = false)
    private String observacion;
    @Column(length = 50, nullable = false)
    private String estado;
    @Column(length = 15, nullable = false)
    private String idUsuario;
    @Column(length = 15, nullable = false)
    private String idReto;


    public MRegistro(UUID id, LocalDate fecha_registro, String observacion, String estado, String idUsuario, String idReto) {
        this.id = id;
        this.fecha_registro = fecha_registro;
        this.observacion = observacion;
        this.estado = estado;
        this.idUsuario = idUsuario;
        this.idReto = idReto;
    }

    public MRegistro() {
    }

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public LocalDate getFecha_registro() {
        return fecha_registro;
    }

    public void setFecha_registro(LocalDate fecha_registro) {
        this.fecha_registro = fecha_registro;
    }

    public String getObservacion() {
        return observacion;
    }

    public void setObservacion(String observacion) {
        this.observacion = observacion;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public String getIdUsuario() {
        return idUsuario;
    }

    public void setIdUsuario(String idUsuario) {
        this.idUsuario = idUsuario;
    }

    public String getIdReto() {
        return idReto;
    }

    public void setIdReto(String idReto) {
        this.idReto = idReto;
    }

    


}



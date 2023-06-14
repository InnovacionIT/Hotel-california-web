import { Component, OnInit } from '@angular/core';
import { RegistroService } from '../../services/registro.service';
import { RegistroRequest } from 'src/app/services/registroRequest';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';


@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']


})

export class RegistroComponent implements OnInit {

  registro: RegistroRequest = {
    nombre: '',
    email: '',
    password: '',
    apellido: '',
    ciudad: '',
    fechaNacimiento: '',
    telefono: ''
  };

  registroForm: FormGroup | undefined;






  constructor(private formBuilder:FormBuilder, private registroService: RegistroService) {}

  ngOnInit(): void {
    this.registroForm = this.formBuilder.group({
      nombre: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      apellido: ['', Validators.required],
      ciudad: [''],
      fechaNacimiento: [''],
      telefono: ['']
    });
  }

  onSubmit() {
    console.log(this.registro); // Imprimir los datos en la consola

    this.registroService.agregarUsuario(this.registro).subscribe(
      (response:any) => {
        console.log('Solicitud POST exitosa', response);
        // Aquí puedes realizar acciones adicionales después de una solicitud exitosa, como redirigir al usuario a una página de éxito o mostrar un mensaje de confirmación.
      },
      (error:any) => {
        console.log('Error en la solicitud POST', error);
        // Manejar los errores de la solicitud, como mostrar un mensaje de error al usuario o realizar acciones de recuperación.
      }
    );
  }
}

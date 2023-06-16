export interface User {
    clienteId:number;
    nombre?:string;
    apellido?:string;
    usuario: string;
    message?:string;
    is_staff:boolean;
    is_superuser:boolean;
}
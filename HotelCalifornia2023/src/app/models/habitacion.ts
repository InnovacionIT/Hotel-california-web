export class Habitacion {
  constructor(
    public habitacionId:number,
    public tipo:string,
    public descripcion:string,
    public servicios:Array<any>,
    public disponible:boolean,
    public precio:number
    ){}
}

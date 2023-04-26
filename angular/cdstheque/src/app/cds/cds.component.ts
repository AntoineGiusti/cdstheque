import { Component, OnInit } from '@angular/core';
import { Cd } from './cd';
import { CdService } from '../cd.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DeleteModalComponent } from '../delete-modal/delete-modal.component';

@Component({
  selector: 'app-cds',
  templateUrl: './cds.component.html',
  styleUrls: ['./cds.component.scss'],

})
export class CdsComponent implements OnInit{

  cds : Cd[] = [];

  constructor(private cdService : CdService, private modalService : NgbModal){};

  ngOnInit(): void {
    this.getCds();
  }

  onSelect(cd : Cd): void {
    this.getCds();
  }

  getCds(): void {
    this.cdService.getCds()
    .subscribe(cds => this.cds = cds);
  }

  add( artist:string, album_name:string, year_published:string): void{
    artist = artist.trim();
    album_name = album_name.trim();
    year_published = year_published.trim();
    if(!artist && !album_name && !year_published){return;}
    this.cdService.addCd({artist, album_name, year_published} as Cd)
      .subscribe(cd => {
        this.cds.push(cd);
      });
  }

  delete(cd : Cd): void {
    let modal = this.modalService.open(DeleteModalComponent,{
      scrollable: true,
    });
    modal.result.then(
      (result)=>{this.cdService.deleteCd(cd.id).subscribe();},
      (reason) =>{}
    );
    modal.componentInstance.cd = cd;


  }


openDeleteModal(artist : string){
    const modalRef = this.modalService.open(DeleteModalComponent);
    modalRef.componentInstance.artist = artist;

    modalRef.result.then(
      (result) => {
        console.log(`fermé avec : ${result}`);
      },
      (reason) => {
        console.log(`Dissmissed ${reason}`);

      }
    )
  }

}



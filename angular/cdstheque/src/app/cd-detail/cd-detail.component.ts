import { Component, OnInit} from '@angular/core';
import { Cd } from "../cds/cd";
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { CdService } from '../cd.service';

@Component({
  selector: 'app-cd-detail',
  templateUrl: './cd-detail.component.html',
  styleUrls: ['./cd-detail.component.scss']
})
export class CdDetailComponent implements OnInit{

  cd : Cd | undefined;

  constructor(
    private route : ActivatedRoute,
    private cdService : CdService,
    private location : Location
  ){}

  ngOnInit(): void {
    this.getCd();
  }

  getCd(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.cdService.getCd(id)
    .subscribe(cd => this.cd = cd);

  }

  save(): void {
    if (this.cd){
      this.cdService.updateCd(this.cd)
      .subscribe(() => this.goBack());
    }
  }

  goBack(): void {
    this.location.back();
  }

}

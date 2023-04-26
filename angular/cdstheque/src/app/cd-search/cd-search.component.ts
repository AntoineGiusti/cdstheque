import { Component, OnInit } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { debounceTime, distinctUntilChanged ,switchMap } from 'rxjs/operators';

import { Cd } from '../cds/cd';
import { CdService } from '../cd.service';

@Component({
  selector: 'app-cd-search',
  templateUrl: './cd-search.component.html',
  styleUrls: ['./cd-search.component.scss']
})
export class CdSearchComponent implements OnInit {


  cds$! : Observable<Cd[]>;
  private searchTerms = new Subject<string>();
  constructor(private cdService : CdService){};

  search(term : string): void {
    this.searchTerms.next(term);
  }

  ngOnInit(): void {
    this.cds$ = this.searchTerms.pipe(
      debounceTime(300),

      distinctUntilChanged(),

      switchMap((term : string) => this.cdService.searchCds(term)),
    );
  }
}

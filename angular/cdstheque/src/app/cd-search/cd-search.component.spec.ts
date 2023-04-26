import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CdSearchComponent } from './cd-search.component';

describe('CdSearchComponent', () => {
  let component: CdSearchComponent;
  let fixture: ComponentFixture<CdSearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CdSearchComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CdSearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

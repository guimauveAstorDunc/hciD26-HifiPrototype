from datetime import datetime
from app import db
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

class TabType(db.Model):
    id :            sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    name :          sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(50), unique=True, nullable=False)
    
    interactions :  sqlo.WriteOnlyMapped['TabClick'] = sqlo.relationship('TabClick', back_populates='tab', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<TabType {self.name}>'

class TabClick(db.Model):
    id :            sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    tab_id :        sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(TabType.id), nullable=False)
    occurred_at :   sqlo.Mapped[datetime] = sqlo.mapped_column(default=datetime.utcnow)
    
    tab = sqlo.relationship('TabType', back_populates='interactions')
    
    def __repr__(self):
        return f'<TabClick tab={self.tab_id} at {self.occurred_at}>'

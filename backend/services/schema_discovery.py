from sqlalchemy import create_engine, MetaData

class SchemaDiscovery:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)
        self.metadata = MetaData()

    def analyze_database(self):
        """Connects to database and returns tables, columns, datatypes, and relationships."""
        self.metadata.reflect(bind=self.engine)
        schema = {}

        for table_name, table_obj in self.metadata.tables.items():
            schema[table_name] = {
                "columns": [col.name for col in table_obj.columns],
                "datatypes": {col.name: str(col.type) for col in table_obj.columns},
                "foreign_keys": [
                    {
                        "column": fk.parent.name,
                        "references_table": fk.column.table.name,
                        "references_column": fk.column.name
                    }
                    for fk in table_obj.foreign_keys
                ],
            }
        return schema
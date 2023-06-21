interface Ort {
  name?: string;
  beschreibung?: string;
  datum?: string;
  standort?: {
    latitude: number;
    longitude: number;
  };
  hauptbild?: string;
  bilder?: Array<{
    url: string;
    beschreibung?: string;
  }>;
  tags?: string[];
}

interface Daten {
  orte: Ort[];
}

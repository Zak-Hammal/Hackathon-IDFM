// ItineraryScreen.js
import { Ionicons } from '@expo/vector-icons';
import React, { useState } from 'react';
import {
  Image,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import referentiel from '../assets/referentiel-des-lignes.json'; // ← ton JSON local

const ItineraryScreen = () => {
  const [departure, setDeparture] = useState('My position');
  const [arrival, setArrival] = useState('Gare de Lyon, Paris 12E Arrondisseme...');
  const [selectedMode, setSelectedMode] = useState('transit');

  // Exemple d’itinéraires avec les SECTIONS
  const itineraries = [
    {
      id: 1,
      startTime: '13:02',
      endTime: '13:17',
      duration: '15 min',
      sections: [
        { id: 's1', type: 'walk', Kcal: 30, CO2: 0 },
        { id: 's2', type: 'metro', idligne: 'C00026', Kcal: 5, CO2: 12 },
        { id: 's3', type: 'RER', idligne: 'C02469', Kcal: 3, CO2: 10 },
      ],
      price: '€2.50',
    },
    {
      id: 2,
      startTime: '13:02',
      endTime: '13:18',
      duration: '16 min',
      sections: [
        { id: 's1', type: 'velo', Kcal: 20, CO2: 0 },
        { id: 's2', type: 'metro', idligne: 'C02452', Kcal: 4, CO2: 15 },
      ],
      price: '€2.50',
    },
    {
      id: 3,
      startTime: '13:01',
      endTime: '13:19',
      duration: '18 min',
      sections: [
        { id: 's1', type: 'walk', Kcal: 40, CO2: 0 },
        { id: 's2', type: 'bus', idligne: 'C02497', Kcal: 3, CO2: 25 },
      ],
      price: '€2',
    },
  ];

  const transportModes = [
    { id: 'transit', icon: 'bus-outline', time: '15m' },
    { id: 'walk', icon: 'walk-outline', time: '36m' },
    { id: 'bike', icon: 'bicycle-outline', time: '15m' },
    { id: 'car', icon: 'car-outline', time: '-' },
  ];

  // Fonction pour récupérer le logo / icône selon type
  const getSectionIcon = (section) => {
    switch (section.type) {
      case 'walk':
        return <Ionicons name="walk-outline" size={18} color="#000" />;
      case 'voiture':
      case 'car':
        return <Ionicons name="car-outline" size={18} color="#000" />;
      case 'velo':
        return <Ionicons name="bicycle-outline" size={18} color="#007AFF" />;
      case 'metro':
      case 'bus':
      case 'RER':
        const ligne = referentiel.find((l) => l.id_line === section.idligne);
        const logoUrl = ligne?.picto?.url;
        if (logoUrl) {
          return (
            <Image
              source={{ uri: logoUrl }}
              style={{ width: 24, height: 24, resizeMode: 'contain' }}
            />
          );
        } else {
          const fallbackIcon =
            section.type === 'metro'
              ? 'subway-outline'
              : section.type === 'RER'
              ? 'train-outline'
              : 'bus-outline';
          return <Ionicons name={fallbackIcon} size={18} color="#007AFF" />;
        }
      default:
        return null;
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />

      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backButton}>
          <Ionicons name="arrow-back" size={24} color="#007AFF" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Itineraries</Text>
        <TouchableOpacity style={styles.settingsButton}>
          <Ionicons name="settings-outline" size={24} color="#007AFF" />
        </TouchableOpacity>
      </View>

      {/* Search Section */}
      <View style={styles.searchSection}>
        <View style={styles.inputContainer}>
          <View style={styles.inputRow}>
            <Text style={styles.label}>Departure</Text>
            <View style={styles.inputWrapper}>
              <Ionicons name="location-outline" size={20} color="#007AFF" style={{ marginRight: 8 }} />
              <Text style={styles.inputText}>{departure}</Text>
            </View>
          </View>

          <TouchableOpacity style={styles.swapButton}>
            <Ionicons name="swap-horizontal-outline" size={20} color="#007AFF" />
          </TouchableOpacity>

          <View style={styles.inputRow}>
            <Text style={styles.label}>Arrival</Text>
            <TextInput
              style={styles.input}
              value={arrival}
              onChangeText={setArrival}
              placeholder="Destination"
            />
          </View>
        </View>

        {/* Transport Mode Selection */}
        <View style={styles.modeSection}>
          {transportModes.map((mode) => (
            <TouchableOpacity
              key={mode.id}
              style={[
                styles.modeButton,
                selectedMode === mode.id && styles.modeButtonActive,
              ]}
              onPress={() => setSelectedMode(mode.id)}
            >
              <Ionicons
                name={mode.icon}
                size={32}
                color={selectedMode === mode.id ? '#007AFF' : '#8E8E93'}
                style={{ marginBottom: 8 }}
              />
              <Text style={styles.modeTime}>{mode.time}</Text>
              {selectedMode === mode.id && <View style={styles.modeIndicator} />}
            </TouchableOpacity>
          ))}
        </View>
      </View>

      {/* Itineraries List */}
      <ScrollView style={styles.itinerariesList}>
        <Text style={styles.sectionTitle}>Suggested itineraries</Text>

        {itineraries.map((itinerary) => (
          <TouchableOpacity key={itinerary.id} style={styles.itineraryCard}>
            <View style={styles.itineraryHeader}>
              <Text style={styles.itineraryTime}>
                {itinerary.startTime} → {itinerary.endTime}
              </Text>
              <Text style={styles.itineraryDuration}>{itinerary.duration}</Text>
            </View>

            {/* Sections */}
            <View style={styles.linesContainer}>
              {itinerary.sections.map((section, index) => (
                <React.Fragment key={index}>
                  <View style={styles.sectionBadge}>
                    {getSectionIcon(section)}
                  </View>
                  {index < itinerary.sections.length - 1 && (
                    <Text style={styles.lineSeparator}>•</Text>
                  )}
                </React.Fragment>
              ))}
            </View>

            <View style={styles.itineraryFooter}>
              <Text style={styles.price}>{itinerary.price}</Text>
            </View>
          </TouchableOpacity>
        ))}
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F5F5F5' },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
  },
  headerTitle: { fontSize: 18, fontWeight: '600', color: '#000' },
  searchSection: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#E5E5E5',
  },
  inputContainer: { backgroundColor: '#F8F8F8', borderRadius: 12, padding: 12 },
  inputRow: { marginBottom: 8 },
  label: { fontSize: 12, color: '#8E8E93', marginBottom: 4 },
  inputWrapper: { flexDirection: 'row', alignItems: 'center' },
  inputText: { fontSize: 16, color: '#000' },
  input: { fontSize: 16, color: '#000', padding: 0 },
  swapButton: { alignSelf: 'flex-end', padding: 8 },
  modeSection: { flexDirection: 'row', marginTop: 16, justifyContent: 'space-between' },
  modeButton: { alignItems: 'center', padding: 12, borderRadius: 12, flex: 1, marginHorizontal: 4 },
  modeButtonActive: { backgroundColor: '#F0F0F0' },
  modeTime: { fontSize: 14, color: '#000', fontWeight: '500' },
  modeIndicator: { position: 'absolute', bottom: 0, left: 0, right: 0, height: 3, backgroundColor: '#007AFF', borderRadius: 2 },
  itinerariesList: { flex: 1, padding: 16 },
  sectionTitle: { fontSize: 20, fontWeight: '600', color: '#000', marginBottom: 16 },
  itineraryCard: { backgroundColor: '#FFF', borderRadius: 12, padding: 16, marginBottom: 12, elevation: 2 },
  itineraryHeader: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 12 },
  itineraryTime: { fontSize: 14, color: '#8E8E93' },
  itineraryDuration: { fontSize: 20, fontWeight: '600', color: '#000' },
  linesContainer: { flexDirection: 'row', alignItems: 'center', marginBottom: 12 },
  sectionBadge: { width: 36, height: 36, borderRadius: 18, justifyContent: 'center', alignItems: 'center', backgroundColor: '#FFF', borderWidth: 1, borderColor: '#E5E5E5' },
  lineSeparator: { fontSize: 16, color: '#8E8E93', marginHorizontal: 4 },
  itineraryFooter: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  price: { fontSize: 16, fontWeight: '600', color: '#5E5CE6' },
});

export default ItineraryScreen;
